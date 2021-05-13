A, B = [int(i) for i in input().split()];

A -= 1;
B -= 1;

def list_2d(H, W, v) :
    return [[v for i in range(W)] for j in range(H)];

ans = list_2d(50, 100, '#') + list_2d(50, 100, '.');

for i in range(1, 50, 2) :
    for j in range(1, 100, 2) :
        if (A) :
            ans[i][j] = '.';
            A -= 1;

for i in range(51, 100, 2) :
    for j in range(1, 100, 2) :
        if (B) :
            ans[i][j] = '#';
            B -= 1;

print(100, 100);
for i in ans :
    for j in i :
        print(j, end = '');
    print();
