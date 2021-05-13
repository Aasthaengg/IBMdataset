#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]


#hashでカウンタを格納する
#ソートして、要素がインクリメントされない箇所を検出する: → 要素がaa

s = input()

h = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

for i in s:
    h[i] += 1

#print(h)
for k,v in h.items():
    if (v == 0):
        print(k)
        exit()

print("None")

