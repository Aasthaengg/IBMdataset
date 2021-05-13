H,W=map(int,input().split())
B=[input() for i in range(H)]
print('#'*(W+2))
for i in range(H):
    A=['#']
    A.append(B[i])
    A.append('#')
    A=''.join(A)
    print(A)
print('#'*(W+2))