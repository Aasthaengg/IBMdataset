import sys;

def mul_matrix(a, b):
    n = len(a);
    m = len(b);
    l = len(b[0]);
    
    ans = [];

    for i in range(n):
        new_row = [];
        for j in range(l):
            sum = 0;
            for k in range(m):
                sum += a[i][k] * b[k][j];

            new_row.append(sum);

        ans.append(new_row);
    
    return ans;

def main():
    n, m, l = [int(i) for i in sys.stdin.readline().strip().split(' ')];
    
    a = [];
    b = [];
    
    for i in range(n):
        data = [int(j) for j in sys.stdin.readline().strip().split(' ')];
        a.append(data);

    for i in range(m):
        data = [int(j) for j in sys.stdin.readline().strip().split(' ')];
        b.append(data);

    ans = mul_matrix(a, b);

    for i in ans:
        print(' '.join([str(j) for j in i]));
        
if __name__ == '__main__':
    main();
