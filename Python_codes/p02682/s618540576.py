a, b, c, k = map(int, input().split()); s,t=0,0;
while(True):
    s=a
    if s>=k:
        t = k;    break
    else:
        t=a;    s += b
        if s>=k:
            break;
        else:
            s += c
            if s >= k:
                d = c-s+k;    t -= d
                break;
print(t)