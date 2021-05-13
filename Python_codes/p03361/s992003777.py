h,w = [int(x) for x in input().split()];
s = [[0 for i in range(w)] for i in range(h)];
for i in range(h) :
    s[i] = input();

ans = 'Yes';
for i in range(h) :
    for j in range(w) :
        if s[i][j] == '.' :
            continue;
        elif i == 0 :
            if j == 0 :
                if s[i+1][j] == '.' and s[i][j+1] == '.' :
                    ans = 'No';
                    break;
            elif j == w-1 :
                if s[i+1][j] == '.' and s[i][j-1] == '.' :
                    ans = 'No';
                    break;
            else :
                if s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.' :
                    ans = 'No';
                    break;
        elif i == h-1 :
            if j == 0 :
                if s[i-1][j] == '.' and s[i][j+1] == '.' :
                    ans = 'No';
                    break;
            elif j == w-1 :
                if s[i-1][j] == '.' and s[i][j-1] == '.' :
                    ans = 'No';
                    break;
            else :
                if s[i-1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.' :
                    ans = 'No';
                    break;
        else :
            if j == 0 :
                if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j+1] == '.' :
                    ans = 'No';
                    break;
            elif j == w-1 :
                if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.' :
                    ans = 'No';
                    break;
            else :
                if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.' :
                    ans = 'No';
                    break;           


print(ans);