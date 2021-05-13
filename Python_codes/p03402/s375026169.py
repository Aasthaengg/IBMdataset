A, B = [int(i) for i in input().split()];

A -= 1;
B -= 1;

ans = [['#' for i in range(100)] for j in range(50)] + [['.' for i in range(100)] for j in range(50)];

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
