first = input()
second = input()
third = input()

d = {}
d["a"]=first
d["b"]=second
d["c"]=third


flag = False
run = "a"
while flag != True:
 
  if d[run] == "":
    flag = True
    print(run.upper())
  else:
    l = len(d[run])
    temp = d[run][0]
    
    d[run] = d[run][1:l]
    
    run = temp