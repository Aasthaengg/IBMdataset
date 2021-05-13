n = int(input());
told,xold,yold = 0,0,0; 
ans = 'Yes';
for i in range(n) :
    tnew,xnew,ynew = [int(x) for x in input().split()];
    dis = abs(xnew-xold) + abs(ynew-yold);
    diff = tnew - told;
    if (diff - dis)%2 == 1 or diff < dis :
        ans = 'No';
        break;
    else :
        told,xold,yold = tnew,xnew,ynew;

print(ans);