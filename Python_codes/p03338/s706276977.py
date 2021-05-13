n = int(input());
s = input();
max = 0;
set = [chr(i) for i in range(97,123)];
for i in range(1,n) :
    x = s[:i];
    y = s[i:];
    cnt = 0;
    #print(x,y,max);
    for ch in set :
        #print(ch);
        if x.find(ch) >= 0 and y.find(ch) >= 0 :
            cnt += 1;
    if cnt > max :
        max = cnt;

print(max);