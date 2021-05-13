st=[]

while True:
  try:
    n=input()
    if n=="":
      break
    st += n.lower()
  except:
    break
   
char = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(char)):
  print(char[i],":",st.count(char[i]))    
