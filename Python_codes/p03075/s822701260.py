n=[int(input()) for i in range(6)]
x=n[5]+1
flg=0
if n[1]-n[0] < x and n[2]-n[0] < x and n[3]-n[0] < x and n[4]-n[0] < x:
    if n[2]-n[1] < x and n[3]-n[1] < x and n[4] - n[1] < x:
        if n[3]-n[2] < x and n[4]-n[2] < x:
            if n[4]-n[3] < x:
                flg=1
print(':(' if flg==0 else 'Yay!')
