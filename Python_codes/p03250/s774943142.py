num = list(input().split())
num.sort(reverse=True)
print(int(''.join(num)[:2]) + int(''.join(num)[2]))