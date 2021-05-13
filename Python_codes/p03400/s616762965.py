n = int(input())
d, x = map(int, input().split())
a_list = []
for _ in range(n):
    a_list.append(int(input()))
    
# print(f"{n} {d} {x}")
# print(a_list)

ans = 0
for a in a_list:
    ans += 1
    ans += (d - 1) // a
    
print(ans + x)