n = int(input())
odd = []
even = []
for i in range(n):
    s = int(input())
    if s % 2:
        odd.append(s)
    else:
        even.append(s)
odd = sorted(odd,reverse = True)

ans = 0
if len(odd) == 0:
    print(0)
    exit()
elif len(odd) == 1:
    ans += odd[0]
    ans += sum(even)
elif len(odd) % 2 == 1:
    ans += sum(odd)
    ans += sum(even)
else:
    ans += sum(odd[:len(odd)-1])
    ans += sum(even)
print(ans)
