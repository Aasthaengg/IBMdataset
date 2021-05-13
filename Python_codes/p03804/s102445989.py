n,m = map(int,input().split())

a_list = []
b_list = []
ans = "No"

for i in range(n):
    a_list.append(input())

for i in range(m):
    b_list.append(input())

for i in range(n-m+1):
    for j in range(n-m+1):
        match = True
        for k in range(m):
            for l in range(m):
                if a_list[i+k][l+j] != b_list[k][l]:
                    match = False
        if match:
            ans = "Yes"
            break

print(ans)
