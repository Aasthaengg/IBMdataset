a = [int(input()) for i in range(5)]
max = 0
kazu = 0
ans = 0
for i in range(5):
    if a[i]%10 == 0: amari = 0
    else: amari = 10-(a[i]%10)
    if amari >= max:
        max = amari
        kazu = i
for i in range(5):
    if i == kazu: pass
    else:
        if a[i]%10 == 0:
            ans+=a[i]
        else:
            ans+=((int(a[i]/10))*10 +10)
print(ans+a[kazu])

