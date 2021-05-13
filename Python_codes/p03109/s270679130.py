s=input()
l=list(map(int,s.split("/")))
if l[0] <=2018 or l[0] ==2019 and (l[1]<=3 or l[1] ==4 and l[2]<=30):
    print('Heisei')
else:
    print("TBD")