s = input()
n = len(s)
if n % 2 != 0:
    print("No")
    quit()

for i in range(n//2):
    if s[2*i:(2*i+2)] != "hi":
        print("No")
        quit()
print("Yes")