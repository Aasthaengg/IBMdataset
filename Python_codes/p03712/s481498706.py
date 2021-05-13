h, w=map(int, input().split())
start=end="#"*(w+2)

print(start)
for i in range(h):
    s=input()
    row="#"+s+"#"
    print(row)

print(end)