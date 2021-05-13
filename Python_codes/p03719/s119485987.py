num = input('').split()

num = [int(x) for x in num] 

ans = 'Yes' if num[0] <= num[2] <= num[1] else 'No'

print(ans)