s=input()
r_s=s[::-1]
c_a=s.find("A")
c_rz=r_s.find("Z")
c_z=len(s)-1-c_rz

print(c_z-c_a+1)