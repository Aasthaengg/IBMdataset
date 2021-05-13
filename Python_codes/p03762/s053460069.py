### D - 井井井 / ###　やりなおし
x, y = [int(i) for i in input().split()]
xl = [int(i) for i in input().split()]
yl = [int(i) for i in input().split()]

xx = sum(  [ i*xl[i] - (x-i-1)*xl[i] for i in range(len(xl)) ]  )
yy = sum(  [ i*yl[i] - (y-i-1)*yl[i] for i in range(len(yl)) ]  )
ans = (xx * yy) % (10**9 + 7)
print(ans)