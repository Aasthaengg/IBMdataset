x, y=map(int, input().split())
end = False
for i in range(x+1):
    if 4*i + 2*(x-i) == y:
        print("Yes")
        end = True
        break
if end == False:
    print("No")