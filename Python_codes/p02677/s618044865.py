import math
a,b,h,m = list(map(int, input().split())) 

short_deg = (((h*60*60+m*60) / (12*60*60)  * 360)+90) % 360
long_deg = (((h*60*60+m*60) / (60*60)  * 360)+90) % 360

short_x = math.cos(short_deg * (math.pi / 180) )*a
short_y = math.sin(short_deg * (math.pi / 180) )*a

long_x = math.cos(long_deg * (math.pi / 180) )*b
long_y = math.sin(long_deg * (math.pi / 180) )*b

l = ((short_x-long_x)**2 + (short_y-long_y)**2 )**0.5
print(l)