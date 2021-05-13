# solution
import io
import math

data = int(input())
result=""
counter=1
if data==0:
	result="0"
while data:
	t=counter
	counter*=-2
	if data%counter:
		data-=t
		result+="1"
	else:
		result+="0"
print(result[::-1])