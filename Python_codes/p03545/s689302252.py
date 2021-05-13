IN = input()
IN = list(map(int, IN))



if IN[0]+IN[1]+IN[2]+IN[3] ==7:
    print(str(IN[0])+"+"+str(IN[1])+"+"+str(IN[2])+"+"+str(IN[3])+"=7")
elif IN[0]-IN[1]+IN[2]+IN[3] ==7:
    print(str(IN[0])+"-"+str(IN[1])+"+"+str(IN[2])+"+"+str(IN[3])+"=7")
elif IN[0]+IN[1]-IN[2]+IN[3] ==7:
    print(str(IN[0])+"+"+str(IN[1])+"-"+str(IN[2])+"+"+str(IN[3])+"=7")
elif IN[0]-IN[1]-IN[2]+IN[3] ==7:
    print(str(IN[0])+"-"+str(IN[1])+"-"+str(IN[2])+"+"+str(IN[3])+"=7")
elif IN[0]+IN[1]+IN[2]-IN[3] ==7:
    print(str(IN[0])+"+"+str(IN[1])+"+"+str(IN[2])+"-"+str(IN[3])+"=7")
elif IN[0]-IN[1]+IN[2]-IN[3] ==7:
    print(str(IN[0])+"-"+str(IN[1])+"+"+str(IN[2])+"-"+str(IN[3])+"=7")
elif IN[0]+IN[1]-IN[2]-IN[3] ==7:
    print(str(IN[0])+"+"+str(IN[1])+"-"+str(IN[2])+"-"+str(IN[3])+"=7")
else: 
    print(str(IN[0])+"+"+str(IN[1])+"+"+str(IN[2])+"-"+str(IN[3])+"=7")


