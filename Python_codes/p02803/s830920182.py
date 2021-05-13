import copy
h,w = map(int, input().split()) 
map=[[-1]*w for i in range(h)]

for i in range(h):
    s=input()
    for j in range(w):
        if s[j]=="#":
            map[i][j]=-2

zanteisaidai=0

def saidaikyori(saisyo_gyou,saisyo_retu,saidaiti):
    map_copy=copy.deepcopy(map)
    map_copy[saisyo_gyou][saisyo_retu]=0
    kyori=0
    while kyori<300:
        for gyou in range(h):
            for retu in range(w):
                if map_copy[gyou][retu]==kyori:
                    if gyou+1<h:
                        if map_copy[gyou+1][retu]==-1:
                            map_copy[gyou+1][retu]=kyori+1
                    if 0<=gyou-1:
                        if map_copy[gyou-1][retu]==-1:
                            map_copy[gyou-1][retu]=kyori+1
                    if retu+1<w:
                        if map_copy[gyou][retu+1]==-1:
                            map_copy[gyou][retu+1]=kyori+1
                    if 0<=retu-1:
                        if map_copy[gyou][retu-1]==-1:
                            map_copy[gyou][retu-1]=kyori+1

        kyori+=1
    
    for gyou in range(h):
        for retu in range(w):
            saidaiti=max(saidaiti,map_copy[gyou][retu])
    return saidaiti

for gyou in range(h):
    for retu in range(w):
        if map[gyou][retu]==-1:
            zanteisaidai=saidaikyori(gyou,retu,zanteisaidai)

print(zanteisaidai)