want, max, time = map(int, input().split())
if want % max == 0:
  required = int(want / max)
else:
  required = int(want / max + 1)
print(required * time)