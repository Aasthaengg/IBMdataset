a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

dis = abs(a-b)
if (v-w) * t >= dis:
    print("YES")
else:
    print("NO")