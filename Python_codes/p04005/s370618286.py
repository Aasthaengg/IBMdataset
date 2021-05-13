a, b, c = map(int, input().split())
ans1 = a*b*(c//2-(c-c//2))
ans2 = a*(b//2-(b-b//2))*c
ans3 = (a//2-(a-a//2))*b*c
print(min([abs(ans1), abs(ans2),abs(ans3)]))
