num_of_match=int(input())
poi_of_1=0
poi_of_2=0
for i in range(num_of_match):
    car_1,car_2=input().split()
    if car_1==car_2:
        poi_of_1+=1
        poi_of_2+=1
    elif car_1>car_2:
        poi_of_1+=3
    elif car_1<car_2:
        poi_of_2+=3
print(poi_of_1,poi_of_2)