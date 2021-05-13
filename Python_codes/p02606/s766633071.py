ent, saida, mul= map(int, input().split())
multiplos=[]
for x in range(ent, saida+1):
    if x%mul==0:
        multiplos.append(x)
print(len(multiplos))