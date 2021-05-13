S = input()
          
Z_list = S.split()
mul = int(Z_list[0])*int(Z_list[1])
mod = mul % 2
if mod == 1:
    print("Odd")
else:
    print("Even")