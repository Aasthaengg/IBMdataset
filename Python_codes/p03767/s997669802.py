n = int(input())
a = sorted(list(map(int, input().split())))
   
ans = a[-2*n :: 2]
print(sum(ans))