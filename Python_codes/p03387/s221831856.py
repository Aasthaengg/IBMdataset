ABC = sorted(list(map(int,input().split())))

ans = ABC[2]-ABC[1]

if (ABC[2]-(ABC[0]+ans))%2 == 0:
    ans += (ABC[2]-(ABC[0]+ans))//2
else:
    ans += (ABC[2]-(ABC[0]+ans))//2+2
print(ans)

