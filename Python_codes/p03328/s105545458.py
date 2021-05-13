a, b = (int(i) for i in input().split())
ans = (b-a-1)*(b-a)/2 - a
print(int(ans))