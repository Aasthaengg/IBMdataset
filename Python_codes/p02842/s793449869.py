n = int(input())
x, mod = divmod(n, 1.08)
print(x if mod == 0 else
      int(x + 1) if int((x+1)*1.08) == n
      else ':(')
