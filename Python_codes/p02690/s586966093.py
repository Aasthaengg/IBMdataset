# +の場合
i = 0
ans = 0
while ans <= 1000000000:
   i += 1
   ans = i**5 - (i-1)**5
# i: 120

# -の場合
i = 0
ans = 0
while ans <= 1000000000:
   i -= 1
   ans = i**5 - (i-1)**5 
# i: -119

n = int(input())
l = [_**5 for _ in range(120)]

for i in range(1,120):
    for j in range(120):
        if l[i] - l[j] == n:
            print(int(l[i]**0.2), int(l[j]**0.2))
            exit()
        if l[i] + l[j] == n:
            print(int(l[i]**0.2), int(-1*l[j]**0.2))
            exit()