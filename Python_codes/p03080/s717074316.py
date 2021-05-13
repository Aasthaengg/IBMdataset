N = int(input())
s = input()
r = len([i for i in s if i == 'R'])
print("Yes" if r > N -r else "No")
