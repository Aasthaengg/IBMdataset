h,w = map(int, input().split())
x = ""
for i in range(w+2):
    x += "#"
print(x)
for i in range(h):
    a = input()
    print("#"+a+"#")
print(x)