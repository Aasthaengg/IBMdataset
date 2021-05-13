H, W = map(int, input().split())
print("".join(["#"]*(W+2)))
for _ in range(H):
    print("#"+input()+"#")
print("".join(["#"]*(W+2)))