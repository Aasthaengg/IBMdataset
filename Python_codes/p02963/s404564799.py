s = int(input())

xl = int(s ** 0.5) + 1
if (xl - 1) * (xl - 1) >= s:
  xl -= 1
  yl = xl
elif (xl - 1) * xl >= s:
  yl = xl - 1
else:
  yl = xl

diff = xl * yl - s
print(*[0, 0, xl, diff, 1, yl])