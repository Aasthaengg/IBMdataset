n = int(input())
A = list(map(int, input().split()))

count_4 = len([a for a in A if a % 4 == 0])
count_2 = len([a for a in A if a % 2 == 0]) - count_4
others = n - (count_4 + count_2)

ans = ""
if count_2 == 0:
    ans = "Yes" if others <= count_4 + 1 else "No"
else:
    ans = "Yes" if others <= count_4 else "No"
print(ans)