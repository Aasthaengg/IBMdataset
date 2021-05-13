h, w = map(int, input().split())
a = ["#"+input()+"#" for i in range(h)]
print("#"*(w+2))
for p in a:
    print(p)
print("#"*(w+2))
