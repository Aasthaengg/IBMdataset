a,b=map(int,input().split())
print(100,100)
b_r=b-1
q=b_r//50
r=b_r%50
for i in range(q):
    print('.'*100)
    print('.#'*50)
print('.'*100)
print('.#'*r+'..'*(50-r))
for i in range(50-2*(q+1)):
    print('.'*100)
a_r=a-1
q=a_r//50
r=a_r%50
for i in range(q):
    print('#'*100)
    print('#.'*50)
print('#'*100)
print('#.'*r+'##'*(50-r))
for i in range(50-2*(q+1)):
    print('#'*100)
