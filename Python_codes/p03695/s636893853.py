N = int(input())
a = list(map(int, input().split()))

fix_color = set()
n_any_color = 0
for color in a:

  if color < 400:
    fix_color.add(400)
  elif color < 800:
    fix_color.add(800)
  elif color < 1200:
    fix_color.add(1200)
  elif color < 1600:
    fix_color.add(1600)
  elif color < 2000:
    fix_color.add(2000)
  elif color < 2400:
    fix_color.add(2400)
  elif color < 2800:
    fix_color.add(2800)
  elif color < 3200:
    fix_color.add(3200)
  else:
    n_any_color += 1

n_min = max(1, len(fix_color))
n_max = len(fix_color) + n_any_color
print(n_min, n_max)
