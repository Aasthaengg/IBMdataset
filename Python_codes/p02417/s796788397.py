alphabet=dict.fromkeys("abcdefghijklmnopqrstuvwxyz",0)
t=list(alphabet)
while True:
    try:
        N = input()
    except:
        break
    N=N.lower()
    z = list(N)
    if N=='':
        break
    for i in range(len(z)):
        for j in range(len(t)):
            if z[i]==t[j]:
                alphabet[t[j]]+=1
for key, value in alphabet.items():
    print(key, ':', value)
