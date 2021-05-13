data=list(input())
if eval(data[0]+"+"+data[1]+"+"+data[2]+"+"+data[3])==7:
    print(data[0]+"+"+data[1]+"+"+data[2]+"+"+data[3]+"=7")
elif eval(data[0]+"+"+data[1]+"+"+data[2]+"-"+data[3])==7:
    print(data[0]+"+"+data[1]+"+"+data[2]+"-"+data[3]+"=7")
elif eval(data[0]+"+"+data[1]+"-"+data[2]+"-"+data[3])==7:
    print(data[0]+"+"+data[1]+"-"+data[2]+"-"+data[3]+"=7")
elif eval(data[0]+"+"+data[1]+"-"+data[2]+"+"+data[3])==7:
    print(data[0]+"+"+data[1]+"-"+data[2]+"+"+data[3]+"=7")
elif eval(data[0]+"-"+data[1]+"+"+data[2]+"+"+data[3])==7:
    print(data[0]+"-"+data[1]+"+"+data[2]+"+"+data[3]+"=7")
elif eval(data[0]+"-"+data[1]+"+"+data[2]+"-"+data[3])==7:
    print(data[0]+"-"+data[1]+"+"+data[2]+"-"+data[3]+"=7")
elif eval(data[0]+"-"+data[1]+"-"+data[2]+"-"+data[3])==7:
    print(data[0]+"-"+data[1]+"-"+data[2]+"-"+data[3]+"=7")
elif eval(data[0]+"-"+data[1]+"-"+data[2]+"+"+data[3])==7:
    print(data[0]+"-"+data[1]+"-"+data[2]+"+"+data[3]+"=7")
else:
    pass