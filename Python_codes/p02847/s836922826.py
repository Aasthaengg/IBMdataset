week_dict = {
    'MON': 1,
    'TUE': 2,
    'WED': 3,
    'THU': 4,
    'FRI': 5,
    'SAT': 6,
    'SUN': 7
}

day_of_week = input()

if day_of_week == 'SUN':
    print(week_dict[day_of_week])

else:
    days_left_to_sunday = 7 - week_dict[day_of_week]
    print(days_left_to_sunday)