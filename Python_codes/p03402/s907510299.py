A,B = map(int,input().split())
A=A-1
B=B-1

lineA=int(A/50)
line = '.#'*50
print(100,100)
for i in range(lineA):
    print(line)
    print('#'*100)

if A%50!=0:
    print('.#'*(A%50),end='')
    print('##'*(50-A%50))
    for _ in range(48-2*lineA):
        print('#'*100)
else:
    for _ in range(49-2*lineA):
        print('#'*100)

print('#'*100)
print('.'*100)

lineB=int(B/50)

for _ in range(lineB):
    print('#.'*50)
    print('.'*100)

if B%50!=0:
    print('#.'*(B%50),end='')
    print('..'*(50-B%50))
    for _ in range(48-2*lineB):
        print('.'*100)
else:
    for _ in range(49-2*lineB):
        print('.'*100)




