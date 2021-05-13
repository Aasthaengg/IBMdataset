c = 0
input()
s = input().split()
input()
t = input().split()
for make in t :
    if make in s : c += 1
print(c)