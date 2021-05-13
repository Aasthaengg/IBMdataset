N,T = map(int,input().split());
t = [int(x) for x in input().split()];

end = 0;
ans = 0;
for i in range(N) :
    if end > t[i] :
        ans += t[i] + T - end;
    else :
        ans += T;
    end = t[i] + T;
    #print(ans,end);

print(ans); 