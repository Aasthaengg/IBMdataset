import math

n = int(input())
a = list(map(int, input().split()))
a.append("#")
start = 0
end = 0

ans = 0

while a[start] != "#" :
  if a[start] != a[end]:
    x = end - start
    if x % 2 == 0:
      ans += x // 2
    else:
      ans += math.floor(x / 2)
  
    start = end

  else:
    end += 1


print(ans)